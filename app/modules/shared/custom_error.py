class CustomError(BaseException):
    def to_response(self):
        return {
            'code': super().args[0],
            'message': super().args[1],
            'status_code': super().args[2]
        }, super().args[2]
    pass