from .model import AbstractSwitch


class OpenAIGPT4(AbstractSwitch):
    """API2D GPT4"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "API2D GPT-4.0中转API"

    @staticmethod
    def get_alias() -> str:
        return "a2dgpt4"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'a2d-gpt-4'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']