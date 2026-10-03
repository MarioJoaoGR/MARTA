"""First-round pairing preserves unsuccessful seeds and separates physical cost."""
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from benchmark.xrepotest import ablation, protocol, report
from benchmark.xrepotest.round_reuse import prepare_first_round
from benchmark.xrepotest.tests.test_ablation import _reference
from benchmark.xrepotest.tests.test_adapter import parsed_repo


def seed(tmp_path, *, has_spec=True):
    ref, manifest, config = _reference(tmp_path)
    config["ablations"] = {"no_coverage_feedback": True}
    config["effective_attempts"] = 3
    target = SimpleNamespace(task_id=0, method=SimpleNamespace(qualified_name="A#run"),
                             spec_path_for_round=lambda rnd: f"ignored/run_r{rnd}_spec.rb")
    src = ref / "tasks/0"
    src.mkdir(parents=True)
    (src / "state.json").write_text(json.dumps({"status":"complete", "task_id":0, "project":"a"}))
    (src / "generation.json").write_text(json.dumps({"times":{"round_0":12, "round_1":8}}))
    common = {"ronda":0, "task_id":0, "project":"a", "metodo":"A#run"}
    events = [{**common, "tipo":"llm", "fase":p, "segundos":2,
               "prompt_tokens":10, "completion_tokens":20}
              for p in ("plano", "dev_primeira", "dev_reparacao")]
    if has_spec:
        events.append({**common, "tipo":"generation_validation", "etapa":"rspec",
                       "valid":True, "code":"RSpec.describe('first') {}"})
    events += [{**common, "tipo":"cobertura", "segundos":1},
               {**common, "ronda":1, "tipo":"llm", "fase":"plano", "segundos":9}]
    (src / "events.jsonl").write_text("\n".join(json.dumps(e) for e in events))
    (src / "marta_specs").mkdir()
    if has_spec:
        (src / "marta_specs/run_r0_spec.rb").write_text("RSpec.describe('first') {}\n")
    (src / "marta_specs/run_r1_spec.rb").write_text("DO NOT COPY")
    (src / "final_spec.rb").write_text("DO NOT COPY FINAL")
    out = tmp_path / "ablation/tasks/0"
    return ref, src, out, target, config


@pytest.mark.parametrize("has_spec", [True, False])
def test_only_round_zero_is_shared_and_absent_spec_is_preserved(tmp_path, has_spec):
    ref, src, out, target, config = seed(tmp_path, has_spec=has_spec)
    provenance = ablation.verify_first_round_reference(ref, config)
    before = {str(p.relative_to(ref)):p.read_bytes() for p in ref.rglob('*') if p.is_file()}
    recorder = Mock()
    audit = prepare_first_round(ref, out, target, 'a', recorder,
                                expected_manifest=provenance['manifest_digest'])
    assert audit['no_spec'] is not has_spec
    assert audit['usage']['generation_seconds'] == 12
    assert sum(p['calls'] for p in audit['usage']['llm_by_phase'].values()) == 3
    assert (out/'marta_specs/run_r0_spec.rb').exists() is has_spec
    assert not (out/'marta_specs/run_r1_spec.rb').exists()
    assert not (out/'final_spec.rb').exists() and not (out/'state.json').exists()
    assert before == {str(p.relative_to(ref)):p.read_bytes() for p in ref.rglob('*') if p.is_file()}
    assert recorder.evento.call_args.kwargs['tipo'] == 'generation_round_reused'


@pytest.mark.parametrize('extra', [dict(no_graph=True), dict(attempts=1),
    dict(ablations={'no_repair':True, 'no_coverage_feedback':True}),
    dict(ablations={'no_type_hints':True, 'no_coverage_feedback':True}),
    dict(ablations={'no_method_retrieval':True, 'no_coverage_feedback':True}),
    dict(ablations={}), dict(max_tokens=99)])
def test_first_round_requires_equivalent_generation_configuration(tmp_path, extra):
    ref, _, _, _, config = seed(tmp_path)
    config.update(extra)
    with pytest.raises(ValueError):
        ablation.verify_first_round_reference(ref, config)


@pytest.mark.parametrize('change', ['running', 'wrong_task', 'wrong_method', 'wrong_spec',
                                     'no_timer', 'no_coverage', 'no_dev', 'empty_spec', 'manifest',
                                     'deleted_accepted_spec', 'edited_spec'])
def test_incomplete_or_incompatible_round_evidence_never_becomes_a_reused_seed(tmp_path, change):
    ref, src, out, target, config = seed(tmp_path)
    expected = protocol.digest(json.loads((ref/'experiment.json').read_text()))
    if change in {'running', 'wrong_task'}:
        data = json.loads((src/'state.json').read_text())
        data.update(status='running' if change=='running' else 'complete',
                    task_id=99 if change=='wrong_task' else 0)
        (src/'state.json').write_text(json.dumps(data))
    elif change == 'no_timer':
        (src/'generation.json').write_text('{"times":{}}')
    elif change in {'wrong_method','no_coverage','no_dev'}:
        events = [json.loads(l) for l in (src/'events.jsonl').read_text().splitlines()]
        if change=='wrong_method':
            for e in events: e['metodo']='Other#run'
        if change=='no_coverage': events=[e for e in events if e['tipo']!='cobertura']
        if change=='no_dev': events=[e for e in events if e.get('fase')!='dev_primeira']
        (src/'events.jsonl').write_text('\n'.join(json.dumps(e) for e in events))
    elif change=='wrong_spec':
        (src/'marta_specs/run_r0_spec.rb').rename(src/'marta_specs/other_r0_spec.rb')
    elif change=='deleted_accepted_spec':
        (src/'marta_specs/run_r0_spec.rb').unlink()
    elif change=='edited_spec':
        (src/'marta_specs/run_r0_spec.rb').write_text('Changed after validation')
    elif change=='empty_spec':
        (src/'marta_specs/run_r0_spec.rb').write_text('')
    else:
        (ref/'experiment.json').write_text('{}')
    with pytest.raises(ValueError):
        prepare_first_round(ref, out, target, 'a', Mock(), expected_manifest=expected)
    assert not out.exists()


def test_reference_reuse_cost_is_separate_and_deduplicated_after_restart(tmp_path):
    ref, src, out, target, config = seed(tmp_path)
    recorder = Mock()
    audit = prepare_first_round(ref, out, target, 'a', recorder,
                               expected_manifest=protocol.digest(json.loads((ref/'experiment.json').read_text())))
    event = {'tipo':'generation_round_reused', **audit}
    (out/'events.jsonl').write_text(json.dumps(event)+'\n'+json.dumps(
        {'tipo':'llm','fase':'dev_primeira','segundos':5,'prompt_tokens':2,'completion_tokens':3}))
    history = out.parents[1]/'interrupted_tasks/0/1'
    history.mkdir(parents=True)
    (history/'events.jsonl').write_text(json.dumps(event))
    data = report.summarize(out.parents[1])
    assert len(data['inherited_first_rounds']) == 1
    assert data['llm_by_phase']['dev_primeira']['calls'] == 1
    assert data['llm_by_phase']['dev_primeira']['seconds'] == 5


@pytest.mark.parametrize('has_spec', [True, False])
def test_pipeline_exports_shared_seed_and_new_rounds_and_resumes_completed_task(
        parsed_repo, tmp_path, monkeypatch, has_spec):
    import asyncio
    import sys
    from types import ModuleType
    from unittest.mock import AsyncMock
    from benchmark.xrepotest import backend, reuse, run, runtime
    from benchmark.xrepotest.tests.test_adapter import task, SUITES, snapshot
    from marta.ruby_backend.ablation import AblationOptions

    rows = [task(42)]
    monkeypatch.setattr(runtime, 'environment_manifest', lambda:None)
    model = SimpleNamespace(aask=AsyncMock(side_effect=AssertionError('no model')), last_call={})
    fake = ModuleType('marta.gptapi'); fake.model=model
    monkeypatch.setitem(sys.modules, 'marta.gptapi', fake)
    reference = tmp_path/'reference'
    reference.mkdir(); (reference/'experiment.json').write_text('{}')
    inventories={'repo':protocol.source_inventory(parsed_repo, rows)}
    with runtime.project_environment(parsed_repo, 'repo'):
        original=backend.XRepoProject(str(parsed_repo), '.', output_root=str(reference/'analysis/repo'),
            code_files=inventories['repo']['code_files'], load_paths=['lib'],
            target_selectors=protocol.selectors(rows), backend=backend.XRepoBackend()).discover()
    target=original.targets[0]
    src=reference/'tasks/42'; src.mkdir(parents=True)
    (src/'state.json').write_text(json.dumps({'task_id':42,'project':'repo','status':'complete' if has_spec else 'no_tests'}))
    (src/'generation.json').write_text('{"times":{"round_0":5}}')
    common={'ronda':0,'task_id':42,'project':'repo','metodo':target.method.qualified_name}
    events=[{**common,'tipo':'llm','fase':p} for p in ('plano','dev_primeira')]
    events.append({**common,'tipo':'cobertura'})
    if has_spec:
        events.append({**common,'tipo':'generation_validation','etapa':'rspec','valid':True,'code':SUITES[0]})
        path=src/'marta_specs'/Path(target.spec_path_for_round(0)).name
        path.parent.mkdir(); path.write_text(SUITES[0]+'\n')
    (src/'events.jsonl').write_text('\n'.join(json.dumps(e) for e in events))
    before=snapshot(reference)
    monkeypatch.setattr(reuse, 'prepare_graph_reuse', lambda *a:None)
    monkeypatch.setattr(reuse, 'prepare_analysis_reuse', lambda *a,**k:SimpleNamespace(documents=None,query=None))
    async def analyze(self, **kw): pass
    monkeypatch.setattr(backend.XRepoProject, 'analyze_summaries', analyze)
    monkeypatch.setattr(backend.XRepoProject, 'build_rag', lambda self,**kw:None)
    generated=[]
    async def generate(self, **kw):
        assert kw['reuse_first_round'] is True
        inherited=Path(self.targets[0].spec_path_for_round(0))
        assert inherited.exists() is has_spec
        dest=Path(self.targets[0].spec_path_for_round(1))
        dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(SUITES[1])
        generated.append(42)
    monkeypatch.setattr(backend.XRepoProject, 'generate_rounds', generate)
    args=SimpleNamespace(repos=parsed_repo.parent, output=tmp_path/'output', work=tmp_path/'work',
        temperature=0.6,no_graph=False,thinking='on',top_p=.95,presence_penalty=0,
        request_timeout=1800,rounds=3,attempts=3,reuse_analysis_from=reference,
        reuse_first_round_from=reference,first_round_manifest=protocol.digest({}),
        **AblationOptions(no_coverage_feedback=True).as_dict())
    asyncio.run(run.pipeline(args, rows, inventories))
    exported=json.loads((args.output/'processed.jsonl').read_text())['response'][0]
    assert SUITES[1] in exported
    assert (SUITES[0] in exported) is has_spec
    assert json.loads((args.output/'tasks/42/first_round_reuse.json').read_text())['no_spec'] is not has_spec
    asyncio.run(run.pipeline(args, rows, inventories))
    assert generated==[42] and snapshot(reference)==before
    model.aask.assert_not_awaited()
