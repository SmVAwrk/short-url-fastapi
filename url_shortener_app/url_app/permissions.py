from typing import Any

from starlette import status
from starlette.exceptions import HTTPException

from ..auth.models import UserTable


def check_owner_or_admin(obj: Any, user: UserTable):
    """
    Функция для проверки прав доступа к объекту.
    (Доступно владельцу или админу)
    """
    if not (obj.get('user_id') == user.id or user.is_superuser):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Permission denied')
