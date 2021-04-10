from ariadne_jwt.decorators import token_auth

extended_type_defs = '''
type UserNode {
    id: ID
    email: String
}
extend type TokenAuth {
    user: UserNode
}
'''

@token_auth
def resolve_token_auth(obj, info, **kwargs):
    return {'user': info.context.get('request').user}