import nltk
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(certifi.where())

nltk.download('punkt', download_dir=nltk.data.path[0], force=True)
nltk.download('averaged_perceptron_tagger',
              download_dir=nltk.data.path[0], force=True)
