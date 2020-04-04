# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from platform.services.user import service_pb2 as platform_dot_services_dot_user_dot_service__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.find_user = channel.unary_unary(
                '/UserService/find_user',
                request_serializer=platform_dot_services_dot_user_dot_service__pb2.Identifier.SerializeToString,
                response_deserializer=platform_dot_services_dot_user_dot_service__pb2.User.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def find_user(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'find_user': grpc.unary_unary_rpc_method_handler(
                    servicer.find_user,
                    request_deserializer=platform_dot_services_dot_user_dot_service__pb2.Identifier.FromString,
                    response_serializer=platform_dot_services_dot_user_dot_service__pb2.User.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def find_user(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/find_user',
            platform_dot_services_dot_user_dot_service__pb2.Identifier.SerializeToString,
            platform_dot_services_dot_user_dot_service__pb2.User.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)