There's a gold badge on **Stack Overflow** called the Fanatic badge. To earn it, you need to log in to Stack Overflow daily for 100 consecutive days. It turns out you can actually build a script to log in to Stack Overflow for you. I came across an [old guide by Alexandru Somai](https://medium.com/coders-do-read/earn-the-fanatic-badge-on-stack-overflow-828d2c46930) that shows a step-by-step process for creating the script. This project essentially follows that guide, as I created the script by following the instructions in the article the only differences is that this one doesnt have the ability to notify via emails.

## Side-note

Most of the steps in the [article](https://medium.com/coders-do-read/earn-the-fanatic-badge-on-stack-overflow-828d2c46930) are fine, but a few changes are required to make this script work:
1. There's no need to install **ChromeDriver** manually; the latest Selenium library includes it. Just proceed with installing **Selenium**.
2. You might need to adjust a few lines of codes when using Selenium, because of the updates that been made to the **Selenium** library:
	```python
	# From this:
	driver.find_element_by_link_text("Log in").click()
	# To this:
	driver.find_element(By.LINK_TEXT, "Log in").click()
	```
1. You might encounter an "IP address mismatch" error when running the `heroku login` command. If so, use `heroku login -i` instead.
	- If your **Heroku** account is set up with multi-factor authentication, you may need to use your Heroku API key as the password (found in your account settings), instead of your account password. Otherwise, you may get an error.
2. Alexandru suggests installing **Chrome** and **ChromeDriver** by defining two buildpacks within our app using the provided command. However, this approach is no longer valid due to a version mismatch between Chrome and ChromeDriver. To resolve this issue, we should use the following command instead:
	```bash
	heroku buildpacks: add https://github.com/heroku/heroku-buildpack-chrome-for-testing
	```
4. Alexandru shows the modified lines of code after installing `webdriver_manager`. However, he mistakenly removed all the required imports. You only need to add the imports for `webdriver_manager` without removing the others.
5. You might encounter an issue when trying to set `heroku config:set STACK_OVERFLOW_PASSWORD` if your password contains special characters. To resolve this, you can set the config manually in the **app settings** on Heroku under the **Config Vars** section of your project/app.

If you apply the changes above, you might be able to run and deploy the script without an issue.

## Quick start

1. Make sure you have already installed **Python**, **pip** and **Chrome**.
2. Run the command below to install all the dependencies from **requirements.txt**.
```sh
    pip install -r requirements.txt
```
3. You can use the `set` command or a library called `python_dotenv` to add your credentials for testing the script.
4. Run `python stack_overflow_page.py` to see if the script work.
5. For deploying, scheduling the script on Heroku, refer to the full step guide for more details.

## Full step-by-step guide

- First part of the guide (without email notification), go [here](https://medium.com/coders-do-read/earn-the-fanatic-badge-on-stack-overflow-828d2c46930).
- The second part with email notification and additional improvement, go [here](https://medium.com/coders-do-read/fanatic-badge-on-stack-overflow-part-two-email-notification-820f5394f8f0).
- Got to [Alexsomai's project repo](https://github.com/alexsomai/stackoverflow-fanatic-badge) for more details.