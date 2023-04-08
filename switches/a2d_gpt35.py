from .model import AbstractSwitch


class OpenAIGPT35(AbstractSwitch):
    """API2D GPT3.5"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "API2D GPT-3.5代理API"

    @staticmethod
    def get_alias() -> str:
        return "a2dgpt3.5"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'a2d-gpt-3.5-turbo'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']