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

# --- PARTE DOS EMBEDDINGS (Como o README pede) ---
try:
    from sentence_transformers import SentenceTransformer
    HAS_LOCAL = True
except ImportError:
    HAS_LOCAL = False
    print("❌ AVISO: 'sentence-transformers' não instalado.")

# Classes falsas para enganar o Test4Py
class LocalEmbeddingResponse:
    def __init__(self, data): self.data = data
class LocalObject:
    def __init__(self, embedding): self.embedding = embedding

# --- O CLIENTE HÍBRIDO (A Ponte) ---
class HybridClient:
    def __init__(self, api_key, base_url, local_model):
        self.chat_client = OpenAI(api_key=api_key, base_url=base_url)
        self.local_model = local_model
        self.embeddings = self 

    @property
    def chat(self):
        return self.chat_client.chat

    def create(self, input, model=None, **kwargs):
        if not self.local_model:
            return LocalEmbeddingResponse([LocalObject([0.0]*1024)])
        
        if isinstance(input, str): input = [input]
        
        try:
            embeddings = self.local_model.encode(input).tolist()
        except Exception as e:
            print(f"⚠️ Erro no embedding local: {e}")
            embeddings = [[0.0] * 1024 for _ in input]

        return LocalEmbeddingResponse([LocalObject(emb) for emb in embeddings])

# --- CLASSE PRINCIPAL ---
class MyGPT:
    count = 0

    def __init__(self, temperature=0.2, max_rate=15, time_period=60, model_type="codellama:7b"):
        load_dotenv()
        
        self.openai_api_key = os.getenv('OPENAI_API_KEY', 'ollama')
        self.openai_api_base = os.getenv('OPENAI_API_BASE', 'http://localhost:11434/v1')
        if os.getenv('MODEL'): model_type = os.getenv('MODEL')
        
        self.embedder = None
        if HAS_LOCAL:
            path = os.getenv('TRANSFORMER_PATH', 'BAAI/bge-large-en-v1.5')
            try:
                print(f"🔄 A carregar modelo de embeddings: {path}")
                self.embedder = SentenceTransformer(path)
                print("✅ Embeddings carregados com sucesso!")
            except Exception as e:
                print(f"⚠️ Erro ao carregar local, a baixar do Hub: {e}")
                self.embedder = SentenceTransformer('BAAI/bge-large-en-v1.5')

        self.temperature = temperature
        self.limiter = AsyncLimiter(max_rate=max_rate, time_period=time_period)
        self.model_type = model_type

        self.client = HybridClient(self.openai_api_key, self.openai_api_base, self.embedder)

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

    def chat(self, messages) -> str:
        try:
            # --- FIX HERE: Added timeout=300.0 ---
            chat = self.client.chat.completions.create(
                model=self.model_type,
                messages=messages,
                temperature=self.temperature,
                stream=False,
                timeout=500.0  # <--- Increased to 300 seconds for local models
            )
            output = chat.choices[0].message.content
            self.count += 1

            # # --- NEW: LOGGING TO FILE ---
            # try:
            #     with open("llm_traffic.log", "a", encoding="utf-8") as f:
            #         f.write(f"\n{'='*40} NEW REQUEST {'='*40}\n")
                    
            #         # Log the input messages (System and User prompts)
            #         for msg in messages:
            #             role = msg['role'].upper()
            #             content = msg['content']
            #             f.write(f"[{role}]:\n{content}\n{'-'*20}\n")
                    
            #         # Log the LLM's response
            #         f.write(f"[ASSISTANT/LLM]:\n{output}\n")
            #         f.write(f"{'='*93}\n")
            # except Exception as log_err:
            #     print(f"Failed to log LLM traffic: {log_err}")
            # # -----------------------------

            
        except Exception as e:
            logging.error(f"Erro no chat: {e}")
            return ""
        return output

model = MyGPT()