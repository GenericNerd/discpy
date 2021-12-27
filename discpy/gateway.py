from __future__ import annotations
from enum import Enum
from json import loads, dumps

class GatewayOpCode(Enum):
    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    RECONNECT = 7
    REQUEST_GUILD_MEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11

    def __repr__(self) -> str:
        return f"<discpy.GatewayOpCode.{self.name} ({self.value})>"

class GatewayEvents(Enum):
    HELLO = "HELLO"
    READY = "READY"
    RESUMED = "RESUMED"
    RECONNECT = "RECONNECT"
    INVALID_SESSION = "INVALID_SESSION"
    CHANNEL_CREATE = "CHANNEL_CREATE"
    CHANNEL_UPDATE = "CHANNEL_UPDATE"
    CHANNEL_DELETE = "CHANNEL_DELETE"
    CHANNEL_PINS_UPDATES = "CHANNEL_PINS_UPDATE"
    THREAD_CREATE = "THREAD_CREATE"
    THREAD_UPDATE = "THREAD_UPDATE"
    THREAD_DELETE = "THREAD_DELETE"
    THREAD_LIST_SYNC = "THREAD_LIST_SYNC"
    THREAD_MEMBER_UPDATE = "THREAD_MEMBER_UPDATE"
    THREAD_MEMBERS_UPDATE = "THREAD_MEMBERS_UPDATE"
    GUILD_CREATE = "GUILD_CREATE"
    GUILD_UPDATE = "GUILD_UPDATE"
    GUILD_DELETE = "GUILD_DELETE"
    GUILD_BAN_ADD = "GUILD_BAN_ADD"
    GUILD_BAN_REMOVE = "GUILD_BAN_REMOVE"
    GUILD_EMOJIS_UPDATE = "GUILD_EMOJIS_UPDATE"
    GUILD_STICKERS_UPDATE = "GUILD_STICKERS_UPDATE"
    GUILD_INTEGRATIONS_UPDATE = "GUILD_INTEGRATIONS_UPDATE"
    GUILD_MEMBER_ADD = "GUILD_MEMBER_ADD"
    GUILD_MEMBER_REMOVE = "GUILD_MEMBER_REMOVE"
    GUILD_MEMBER_UPDATE = "GUILD_MEMBER_UPDATE"
    GUILD_MEMBERS_CHUNK = "GUILD_MEMBERS_CHUNK"
    GUILD_ROLE_CREATE = "GUILD_ROLE_CREATE"
    GUILD_ROLE_DELETE = "GUILD_ROLE_DELETE"
    GUILD_SCHEDULED_EVENT_CREATE = "GUILD_SCHEDULED_EVENT_CREATE"
    GUILD_SCHEDULED_EVENT_UPDATE = "GUILD_SCHEDULED_EVENT_UPDATE"
    GUILD_SCHEDULED_EVENT_DELETE = "GUILD_SCHEDULED_EVENT_DELETE"
    GUILD_SCHEDULED_EVENT_USER_ADD = "GUILD_SCHEDULED_EVENT_USER_ADD"
    GUILD_SCHEDULED_EVENT_USER_REMOVE = "GUILD_SCHEDULED_EVENT_USER_REMOVE"
    INTEGRATION_CREATE = "INTEGRATION_CREATE"
    INTEGRATION_UPDATE = "INTEGRATION_UPDATE"
    INTEGRATION_DELETE = "INTEGRATION_DELETE"
    INTERACTION_CREATE = "INTERACTION_CREATE"
    INVITE_CREATE = "INVITE_CREATE"
    INVITE_DELETE = "INVITE_DELETE"
    MESSAGE_CREATE = "MESSAGE_CREATE"
    MESSAGE_UPDATE = "MESSAGE_UPDATE"
    MESSAGE_DELETE = "MESSAGE_DELETE"
    MESSAGE_DELETE_BULK = "MESSAGE_DELETE_BULK"
    MESSAGE_REACTION_ADD = "MESSAGE_REACTION_ADD"
    MESSAGE_REACTION_REMOVE = "MESSAGE_REACTION_REMOVE"
    MESSAGE_REACTION_REMOVE_ALL = "MESSAGE_REACTION_REMOVE_ALL"
    MESSAGE_REACTION_REMOVE_EMOJI = "MESSAGE_REACTION_REMOVE_EMOJI"
    PRESENCE_UPDATE = "PRESENCE_UPDATE"
    STAGE_INSTANCE_CREATE = "STAGE_INSTANCE_CREATE"
    STAGE_INSTANCE_DELETE = "STAGE_INSTANCE_DELETE"
    STAGE_INSTANCE_UPDATE = "STAGE_INSTANCE_UPDATE"
    TYPING_START = "TYPING_START"
    USER_UPDATE = "USER_UPDATE"
    VOICE_STATE_UPDATE = "VOICE_STATE_UPDATE"
    VOICE_SERVER_UPDATE = "VOICE_SERVER_UPDATE"
    WEBHOOKS_UPDATE = "WEBHOOKS_UPDATE"

    def __repr__(self) -> str:
        return f"<discpy.GatewayEvents.{self.name}>"

class GatewayPayload:
    def __init__(self, opcode: GatewayOpCode, sequence: int = None, eventName: GatewayEvents = None, data: dict = None):
        self.op = opcode
        self.s = sequence
        self.t = eventName
        self.d = data

    def __repr__(self) -> str:
        return f"<discpy.GatewayPayload op={self.op} s={self.s} t={self.t} d={self.d}>"

    def __eq__(self, other: GatewayPayload) -> bool:
        return self.__dict__ == other.__dict__

    def toJSON(self) -> str:
        if self.t is None:
            event = None
        else:
            event  = self.t.value
        return dumps({"op": self.op.value, "s": self.s, "t": event, "d": self.d})
    
    @staticmethod
    def fromJSON(data: str) -> GatewayPayload:
        data = loads(data)
        if data.get("t") is None:
            event = None
        else:
            event = GatewayEvents(data["t"])
        return GatewayPayload(GatewayOpCode(data["op"]), data.get("s"), event, data.get("d"))

class Gateway:
    def __init__(self):
        pass