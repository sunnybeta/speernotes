from fastapi import HTTPException, status

SomethingWentWrong = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something Went Wrong")
NotFound = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found: Thank you Mario but your princess is in another castle")
Forbidden = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden: You do not have the permission to do that")
Unauthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized: Backtraced VPN IP will be reported. Good Luck!")
Conflict = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Whoops: This usename / email already exists")
