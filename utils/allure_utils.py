import allure

def log_response(response):
    try:
        body = response.json()
    except Exception:
        body = response.text

    allure.attach(
        str(response.request.url),
        name="Request URL",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        str(body),
        name="Response",
        attachment_type=allure.attachment_type.JSON,
    )

