# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from aiolimiter import AsyncLimiter
# import asyncio
# import logging


# class MyGPT:
#     count = 0

#     def __init__(self, temperature=0.0, max_rate=300, time_period=20, model_type="gpt-4o"):
#         load_dotenv()
#         self.openai_api_key = os.getenv('OPENAI_API_KEY')
#         self.openai_api_base = os.getenv('OPENAI_API_BASE')
#         if os.getenv('MODEL'):
#             model_type = os.getenv('MODEL')
#         self.temperature = temperature
#         self.limiter = AsyncLimiter(max_rate=max_rate, time_period=time_period)
#         self.model_type = model_type

#         self.client = OpenAI(
#             api_key=self.openai_api_key,
#             base_url=self.openai_api_base,
#         )

#         logging.basicConfig(
#             filename='error.log',
#             level=logging.ERROR,
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             filemode='w'
#         )

#     async def aask(self, system, user):
#         async with self.limiter:
#             messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
#             return await asyncio.to_thread(self.chat, messages)

#     def chat(self, messages)->str:
#         try:
#             chat = self.client.chat.completions.create(
#                 model=self.model_type,
#                 messages=messages,
#                 temperature=self.temperature,
#                 stream=False
#             )
#             output = chat.choices[0].message.content
#             self.count += 1
#         except BaseException as e:
#             logging.error(e)
#             return ""
#         return output

# model = MyGPT()

#Com o ollama(aplicação)
import os
import logging
from dotenv import load_dotenv
from aiolimiter import AsyncLimiter
import asyncio
from openai import OpenAI

from marta.recorder import recoder
from marta.llm_response import ChatReply

# NOTA: os embeddings (RAG) são tratados exclusivamente por marta/embedding.py
# (HuggingFaceEmbedder). O antigo HybridClient/SentenceTransformer aqui carregava
# um SEGUNDO modelo bge-large que nunca era usado — removido para poupar
# tempo de arranque e memória (competia com o Ollama pela CPU/GPU).


# --- CLASSE PRINCIPAL ---
class MyGPT:
    count = 0
    response_api = True

    def __init__(self, temperature=0.2, max_rate=300, time_period=20, model_type="codellama:7b"):
        load_dotenv()

        self.openai_api_key = os.getenv('OPENAI_API_KEY', 'ollama')
        self.openai_api_base = os.getenv('OPENAI_API_BASE', 'http://localhost:11434/v1')
        if os.getenv('MODEL'): model_type = os.getenv('MODEL')

        self.temperature = temperature
        self.limiter = AsyncLimiter(max_rate=max_rate, time_period=time_period)
        self.model_type = model_type
        # Detalhe da última chamada (tokens, finish_reason, erro) — ver chat().
        self.last_call = None

        # Teto de geração: trava respostas em loop de modelos locais (o objetivo
        # é cortar o runaway, não o output legítimo). Override via LLM_MAX_TOKENS;
        # 'none'/0 desativa o limite.
        _mt = os.getenv('LLM_MAX_TOKENS', '2048')
        try:
            _mt_int = int(_mt)
        except (TypeError, ValueError):
            _mt_int = 2048
        self.max_tokens = _mt_int if _mt_int > 0 else None

        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.openai_api_base)

        logging.basicConfig(
            filename='error.log',
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='w'
        )

    async def aask(self, system, user):
        async with self.limiter:
            messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
            return await asyncio.to_thread(self.chat, messages)

    async def aask_result(self, system, user) -> ChatReply:
        async with self.limiter:
            messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
            return await asyncio.to_thread(self.chat_result, messages)

    def chat_result(self, messages) -> ChatReply:
        """One logical SDK request; metadata travels with the returned response."""
        try:
            kwargs = dict(
                model=self.model_type,
                messages=messages,
                temperature=self.temperature,
                stream=False,
                timeout=getattr(self, 'request_timeout', 500.0),
            )
            if self.max_tokens is not None:
                kwargs['max_tokens'] = self.max_tokens
            # Optional per-client setting; legacy runs leave it unspecified.
            effort = getattr(self, 'reasoning_effort', None)
            if effort is not None:
                # openai 1.42 (the pinned environment) predates this named
                # argument. extra_body sends the same JSON without an upgrade.
                kwargs['extra_body'] = {'reasoning_effort': effort}
            for parameter in ('top_p', 'presence_penalty'):
                value = getattr(self, parameter, None)
                if value is not None:
                    kwargs[parameter] = value

            chat = self.client.chat.completions.create(**kwargs)
            usage = getattr(chat, 'usage', None)
            return ChatReply(
                text=chat.choices[0].message.content,
                prompt_tokens=getattr(usage, 'prompt_tokens', None),
                completion_tokens=getattr(usage, 'completion_tokens', None),
                finish_reason=getattr(chat.choices[0], 'finish_reason', None),
            )
        except Exception as error:
            logging.error(f"Erro no chat: {error}")
            return ChatReply(text="", error=repr(error)[:200])

    def chat(self, messages) -> str:
        """Legacy Python/string API; preserves its existing global counters."""
        result = self.chat_result(messages)
        details = result.details()
        self.last_call = details
        if result.error is None:
            self.count += 1
            if result.prompt_tokens is not None or result.completion_tokens is not None:
                recoder.score.add_tokens(details['prompt_tokens'], details['completion_tokens'])
        return result.text

model = MyGPT()
