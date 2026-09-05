'''
python -m pytest .\test\unit_test\test_account_service.py
'''

from service.account_service import AccountService

def test_hash_password_creates_a_verifiable_hash():
	service = AccountService()
	password = "correct horse battery staple"

	hashed_password = service.hash_password(password)

	assert hashed_password != password
	assert service.verify_password(password, hashed_password) is True


def test_hash_password_uses_a_new_salt_each_time():
	service = AccountService()
	password = "correct horse battery staple"

	first_hash = service.hash_password(password)
	second_hash = service.hash_password(password)

	assert first_hash != second_hash
	assert service.verify_password(password, first_hash) is True
	assert service.verify_password(password, second_hash) is True


def test_verify_password_rejects_the_wrong_password():
	service = AccountService()
	hashed_password = service.hash_password("correct password")

	assert service.verify_password("wrong password", hashed_password) is False
