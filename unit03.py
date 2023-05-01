

import ssl
import certifi
import nltk

from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI

import os
os.environ["OPENAI_API_KEY"] = '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'


# 設置 SSL 憑證路徑
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(certifi.where())
# 下載相關資料集
nltk.download('punkt', download_dir=nltk.data.path[0], force=True)
nltk.download('averaged_perceptron_tagger',
              download_dir=nltk.data.path[0], force=True)


# 导入文本
loader = UnstructuredFileLoader("/unit03/unit03.txt")

# 将文本转成 Document 对象
document = loader.load()
print(f'documents:{len(document)}')

# 初始化文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0
)

# 切分文本
split_documents = text_splitter.split_documents(document)
print(f'documents:{len(split_documents)}')

# 加载 llm 模型
llm = OpenAI(model_name="text-davinci-003", max_tokens=1500)

# 创建总结链
chain = load_summarize_chain(llm, chain_type="refine", verbose=True)

# 执行总结链，（为了快速演示，只总结前5段）
chain.run(split_documents[:3])
