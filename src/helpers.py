#!/usr/bin/env python3
def validate_uuid(value: str):
    import uuid
            try:
uuid.UUID(value)
return True
except ValueError:
 return False
