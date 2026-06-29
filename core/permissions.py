ALLOWED_ROLES = {
    1505029296823992330,
    1505029873188737165,
    1505030364459176026,
    1505030227984781392,
}


def has_permission(member):

    return any(
        role.id in ALLOWED_ROLES
        for role in member.roles
    )