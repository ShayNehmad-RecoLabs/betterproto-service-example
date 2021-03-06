# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: example/services/v1/common_enum.proto, example/services/v1/different_service.proto, example/services/v1/user_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class DataSource(betterproto.Enum):
    DATA_SOURCE_UNSPECIFIED = 0


class SchmooserRole(betterproto.Enum):
    ROLE_UNSPECIFIED = 0
    ROLE_VIEWER = 10
    ROLE_IT = 20
    ROLE_ADMIN = 30
    ROLE_SUPER_ADMIN = 100


class UserRole(betterproto.Enum):
    ROLE_UNSPECIFIED = 0
    ROLE_VIEWER = 10
    ROLE_IT = 20
    ROLE_ADMIN = 30
    ROLE_SUPER_ADMIN = 100


@dataclass(eq=False, repr=False)
class AddSchmooserRequest(betterproto.Message):
    email_address: str = betterproto.string_field(1)
    user_roles: List["SchmooserRole"] = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class AddSchmooserResponse(betterproto.Message):
    user: "Schmooser" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ListSchmoosersRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ListSchmoosersResponse(betterproto.Message):
    users: List["Schmooser"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Schmooser(betterproto.Message):
    user_id: str = betterproto.string_field(1)
    # / Schmooser's personal info
    email_address: str = betterproto.string_field(10)
    # / Schmooser's system info
    user_roles: List["SchmooserRole"] = betterproto.enum_field(20)
    # / Schmooser metadata
    creation_time: datetime = betterproto.message_field(30)
    last_login_time: datetime = betterproto.message_field(31)


@dataclass(eq=False, repr=False)
class GetSchmooserRequest(betterproto.Message):
    user_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetSchmooserResponse(betterproto.Message):
    user: "Schmooser" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class AddUserRequest(betterproto.Message):
    email_address: str = betterproto.string_field(1)
    user_roles: List["UserRole"] = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class AddUserResponse(betterproto.Message):
    user: "User" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ListUsersRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ListUsersResponse(betterproto.Message):
    users: List["User"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class User(betterproto.Message):
    user_id: str = betterproto.string_field(1)
    # / User's personal info
    email_address: str = betterproto.string_field(10)
    # / User's system info
    user_roles: List["UserRole"] = betterproto.enum_field(20)
    # / User metadata
    creation_time: datetime = betterproto.message_field(30)
    last_login_time: datetime = betterproto.message_field(31)


@dataclass(eq=False, repr=False)
class GetUserRequest(betterproto.Message):
    user_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetUserResponse(betterproto.Message):
    user: "User" = betterproto.message_field(1)
    data_source: "DataSource" = betterproto.enum_field(2)


class SchmooserServiceStub(betterproto.ServiceStub):
    async def add_schmooser(
        self,
        *,
        email_address: str = "",
        user_roles: Optional[List["SchmooserRole"]] = None,
    ) -> "AddSchmooserResponse":
        user_roles = user_roles or []

        request = AddSchmooserRequest()
        request.email_address = email_address
        request.user_roles = user_roles

        return await self._unary_unary(
            "/example.services.v1.SchmooserService/AddSchmooser",
            request,
            AddSchmooserResponse,
        )

    async def list_schmoosers(self) -> "ListSchmoosersResponse":

        request = ListSchmoosersRequest()

        return await self._unary_unary(
            "/example.services.v1.SchmooserService/ListSchmoosers",
            request,
            ListSchmoosersResponse,
        )

    async def get_schmooser(self, *, user_id: str = "") -> "GetSchmooserResponse":

        request = GetSchmooserRequest()
        request.user_id = user_id

        return await self._unary_unary(
            "/example.services.v1.SchmooserService/GetSchmooser",
            request,
            GetSchmooserResponse,
        )


class UserServiceStub(betterproto.ServiceStub):
    async def add_user(
        self, *, email_address: str = "", user_roles: Optional[List["UserRole"]] = None
    ) -> "AddUserResponse":
        user_roles = user_roles or []

        request = AddUserRequest()
        request.email_address = email_address
        request.user_roles = user_roles

        return await self._unary_unary(
            "/example.services.v1.UserService/AddUser", request, AddUserResponse
        )

    async def list_users(self) -> "ListUsersResponse":

        request = ListUsersRequest()

        return await self._unary_unary(
            "/example.services.v1.UserService/ListUsers", request, ListUsersResponse
        )

    async def get_user(self, *, user_id: str = "") -> "GetUserResponse":

        request = GetUserRequest()
        request.user_id = user_id

        return await self._unary_unary(
            "/example.services.v1.UserService/GetUser", request, GetUserResponse
        )


class SchmooserServiceBase(ServiceBase):
    async def add_schmooser(
        self, email_address: str, user_roles: Optional[List["SchmooserRole"]]
    ) -> "AddSchmooserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_schmoosers(self) -> "ListSchmoosersResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_schmooser(self, user_id: str) -> "GetSchmooserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_add_schmooser(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "email_address": request.email_address,
            "user_roles": request.user_roles,
        }

        response = await self.add_schmooser(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_list_schmoosers(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.list_schmoosers(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_get_schmooser(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "user_id": request.user_id,
        }

        response = await self.get_schmooser(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/example.services.v1.SchmooserService/AddSchmooser": grpclib.const.Handler(
                self.__rpc_add_schmooser,
                grpclib.const.Cardinality.UNARY_UNARY,
                AddSchmooserRequest,
                AddSchmooserResponse,
            ),
            "/example.services.v1.SchmooserService/ListSchmoosers": grpclib.const.Handler(
                self.__rpc_list_schmoosers,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListSchmoosersRequest,
                ListSchmoosersResponse,
            ),
            "/example.services.v1.SchmooserService/GetSchmooser": grpclib.const.Handler(
                self.__rpc_get_schmooser,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetSchmooserRequest,
                GetSchmooserResponse,
            ),
        }


class UserServiceBase(ServiceBase):
    async def add_user(
        self, email_address: str, user_roles: Optional[List["UserRole"]]
    ) -> "AddUserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_users(self) -> "ListUsersResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_user(self, user_id: str) -> "GetUserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_add_user(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "email_address": request.email_address,
            "user_roles": request.user_roles,
        }

        response = await self.add_user(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_list_users(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.list_users(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_get_user(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "user_id": request.user_id,
        }

        response = await self.get_user(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/example.services.v1.UserService/AddUser": grpclib.const.Handler(
                self.__rpc_add_user,
                grpclib.const.Cardinality.UNARY_UNARY,
                AddUserRequest,
                AddUserResponse,
            ),
            "/example.services.v1.UserService/ListUsers": grpclib.const.Handler(
                self.__rpc_list_users,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListUsersRequest,
                ListUsersResponse,
            ),
            "/example.services.v1.UserService/GetUser": grpclib.const.Handler(
                self.__rpc_get_user,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetUserRequest,
                GetUserResponse,
            ),
        }
