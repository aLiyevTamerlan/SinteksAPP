class Mediator:
    def __init__(self):
        self.handlers = {}
    
    async def register(
        self,
        command_type,
        handler,
    ):
        self.handlers[command_type] = handler

    async def send(self, command):
        command_type = type(command)
        handler = self.handlers.get(command_type)

        if not handler:
            raise ValueError(f"No handler registered for command type: {command_type}")

        return await handler.handle(command)