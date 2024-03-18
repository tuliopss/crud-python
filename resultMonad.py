class ResultMonad:
    def __init__(self, value, success=True):
        self.value = value
        self.success = success

    def bind(self, func):
        if self.success:
            try:
                result = func(self.value)
                return ResultMonad(result)
            except Exception as e:
                return ResultMonad(str(e), success=False)
        else:
            return self
