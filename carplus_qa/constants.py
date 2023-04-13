# flake8: noqa
# The description of the chain you are exposing. This will be used by ChatGPT to decide when to call it.
ENDPOINT_DESCRIPTION = "Ask questions about 格上租車's services!"
# The name of your endpoint that you are exposing.
ENDPOINT_NAME = "ask-carplus"
# The input key for the chain. The user input will get mapped to this key.
INPUT_NAME = "query"
# The output key for the chain. The final response will take this key from the chain output.
OUTPUT_KEY = "result"
# Name of the overall service to expose to the model.
NAME_FOR_MODEL = "carplusQABot"
# Name of the overall service to expose to humans.
NAME_FOR_HUMAN = "格上小幫手"
# Description of the overall service to expose to the model.
DESCRIPTION_FOR_MODEL = "This plugin provides access to a QA Bot to answer questions about services provided by Carplus, a ride-sharing company in Taiwan."
# Description of the overall service to expose to humans.
DESCRIPTION_FOR_HUMAN = "有關格上租車的問題，都可以問我！"
