class Config:
    __user_agent = "inter-pixpy-samueljansem"
    __api_base_url = "https://cdpj.partners.bancointer.com.br"
    __mime_json = "application/json"
    __mime_form = "application/x-www-form-urlencoded"

    @property
    def user_agent(self):
        return self.__user_agent

    @property
    def api_base_url(self):
        return self.__api_base_url

    @property
    def mime_json(self):
        return self.__mime_json

    @property
    def mime_form(self):
        return self.__mime_form
