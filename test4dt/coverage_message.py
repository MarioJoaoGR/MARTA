import json
import os.path
import subprocess
from dotenv import load_dotenv


class MyCoverage:
    def __init__(self, path, test_path, source_dir):
        self.path = path
        self.test_path = test_path
        self.source_dir = source_dir
        load_dotenv()

    def get_coverage(self):
        cwd_path = os.path.abspath(self.path)
        
        # 1. Configurar o PYTHONPATH (exatamente como no testcase_react)
        env = os.environ.copy()
        current_pp = env.get('PYTHONPATH', '')
        env['PYTHONPATH'] = f"{cwd_path}:{current_pp}" if current_pp else cwd_path

        # 2. Executar o Coverage + Pytest COM A VACINA (-c /dev/null --rootdir)
        args = [
            os.getenv('USER_PYTHON_PATH', 'python'), '-m', 'coverage', 'run', '-m', '--branch', 
            f'--source={self.source_dir}', 'pytest', '--continue-on-collection-errors', 
            '-c', '/dev/null', '--rootdir', cwd_path, # <--- A VACINA ENTRA AQUI
            self.test_path
        ]
        
        process = subprocess.Popen(args, cwd=cwd_path, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        # 3. Gerar o JSON do Coverage
        args_json = [os.getenv('USER_PYTHON_PATH', 'python'), '-m', 'coverage', 'json', '-i', '-o', f'{self.test_path}/coverage.json']
        process_json = subprocess.Popen(args_json, cwd=cwd_path, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process_json.communicate()

        # 4. Ler o resultado (Mantendo a estrutura da baseline)
        with open(os.path.join(self.path, f'{self.test_path}/coverage.json'), 'r') as f:
            return json.load(f)


class CoverageMessage:
    def __init__(self, missing_lines, summary):
        self.missing_lines = missing_lines
        self.summary = summary

    def get_missing_lines(self):
        return self.summary['missing_lines']

    def get_covered_lines(self):
        return self.summary['covered_lines']

    def get_missing_branches(self):
        return self.summary['missing_branches']

    def get_covered_branches(self):
        return self.summary['covered_branches']

    def format_missing_lines(self):
        if not self.missing_lines:
            return ""
        ranges = []
        start = end = self.missing_lines[0]
        for num in self.missing_lines[1:]:
            if num == end + 1:
                end = num
            else:
                ranges.append(f"{start}-{end}" if start != end else f"{start}")
                start = end = num
        ranges.append(f"{start}-{end}" if start != end else f"{start}")
        return ", ".join(ranges)
