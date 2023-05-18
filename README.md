# 文件
## LangChain 中文入门教程
+ https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide
## LangChain 中文入门教程 gitbook
+ https://liaokong.gitbook.io/llm-kai-fa-jiao-cheng/
## Welcome to LangChain 使用手冊
+ https://python.langchain.com/en/latest/index.html

# open api key
+ blackjtsai (langchain)
  + sk-KxHYJDhOpSfEmhiVR2SKT3BlbkFJ58EB8VQ9S8BxEHgQp4vm1


# 創建 , 啟用 , 安裝依賴 , 離開 venv
+ python --v
+ pip install virtuale (安裝)

# ---建立虛擬專案環境----
+ $ python -m venv venv  (建立)
+ $ venv\Scripts\activate (進入) or mac source venv/bin/activate

+ $ python  -m pip install --upgrade pip
+ $ pip install langchain
+ $ pip install openai

+ $ deactivate
+ 設定還環境變量
  + $ export OPENAI_API_KEY='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'
  + $ export SERPAPI_API_KEY='fd5b9cb6c89dcb45cc70ac8ff60ed759af5db8d8eedde7219bf8ba7ccb55f494'


# unit01 完成一次问答
## 知識點
+ openai key
```
import os
os.environ["OPENAI_API_KEY"] = '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'
```

# unit02 通过 Google 搜索并返回答案
## 知識點
+ Serpapi 来进行实现，Serpapi 提供了 google 搜索的 api 接口。
+ Serpapi 官网上注册一个用户，https://serpapi.com/ 并复制他给我们生成 api key。
+ Chatgpt 只能给官方赚钱，而 Openai API 能给我赚钱
+ $ pip install google-search-results

# unit03 对超长文本进行总结
+ 文本超过了 api 最大的 token 限制就会报错
+ 通过 tiktoken 计算并分割,将各段发送给 api 进行总结
+ LangChain，他很好的帮我们处理了这个过程
+ chain_type="refine" chain_type="refine"
  + map_reduce: 这个方式会先将每个 document 进行总结，最后将所有 document 总结出的结果再进行一次总结。
  + stuff: 这种最简单粗暴，会把所有的 document 一次全部传给 llm 模型进行总结。
  + refine: 这种方式会先总结第一个 document，然后在将第一个 document 总结出的内容和第二个 document 一起发给 llm 模型在进行总结，以此类推。
  + map_rerank: 这种一般不会用在总结的 chain 上，而是会用在问答的 chain 上，他其实是一种搜索答案的匹配方式。
+ $ pip install unstructured
+ $ pip install --upgrade pdfminer.six
+ 片段說說明
```
import nltk
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(certifi.where())

nltk.download('punkt', download_dir=nltk.data.path[0], force=True)
nltk.download('averaged_perceptron_tagger',
              download_dir=nltk.data.path[0], force=True)
```
這段程式碼的作用是下載並安裝nltk中的 punkt 和 averaged_perceptron_tagger 資料集。而由於下載資料集需要通過SSL驗證，但是系統中的SSL證書出現了問題，無法通過驗證，所以在程式中需要先將ssl驗證設置為不驗證證書。具體地，程式的執行過程如下：

  + import nltk：引入nltk模組。
  + import certifi：引入certifi模組，這個模組可以提供一個安全的SSL憑證路徑。
  + import ssl：引入ssl模組，這個模組可以提供用於建立安全連接的函數和方法。
  + ssl._create_default_https_context = ssl._create_unverified_context：將ssl的驗證設置為不驗證證書。
  + nltk.data.path.append(certifi.where())：設置nltk的資料路徑，使用certifi模組提供的SSL憑證路徑。
  + nltk.download("punkt")：下載並安裝nltk中的 punkt 資料集。
  + nltk.download("averaged_perceptron_tagger")：下載並安裝nltk中的 averaged_perceptron_tagger 資料集。

# unit04 构建本地知识库问答机器人
+ $ pip install chromadb
+ $ brew update
+ $ brew upgrade llvm
+ $ pip install hnswlib --no-compile -v


#

