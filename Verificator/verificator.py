import requests

TOKEN = 'c261e2978866dc40cbaa8f9cc6bb8e0798a994c5'


def prepare_headers():
    return {
        'Authorization': 'token {}'.format(TOKEN),
        'Content-Type': "application/json",
        'Accept': 'application/vnd.github.v3+json'
    }


def get_all_user_prs(user_login, repo_name, pr_state):
    url = 'https://api.github.com/repos'
    prs_url = url + "/{}/{}/pulls".format(user_login, repo_name)
    r = requests.get(prs_url, headers=prepare_headers())
    pr_nums = []
    for item in r.json():
        pr_nums.append(prs_url + '/{}'.format(str(item['number'])))
    return pr_nums


def get_all_pr_commits(pr):
    commit_url = pr + '/commits'
    commits = []
    for item in requests.get(commit_url, headers=prepare_headers()).json():
        commits.append(item['commit']['message'])
    return commits


def check_prefixes(title):
    TASK_PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS', 'ITERATOR']
    GROUP = ['1021', '1022']
    ACTION = ['Added', 'Deleted', 'Refactored', 'Deleted', 'Moved']
    print(title)
    try:
        title_parts = title.split(' ')
        title_group = title_parts[0].split('-')
        if title_group[1] not in GROUP:
            return 'Error in Group'
        if title_group[0] not in TASK_PREFIX:
            return 'Error in Prefix'
        if title_parts[1] not in ACTION:
            return 'Error in Action'
    except:
        return 'Wrong structure'


def send_pr_comment(pr, message_error):
    payload = {
        'comment[body]': message_error
    }
    r = requests.post(pr, data=payload)


def verify_pr(pr):
    for item in get_all_pr_commits(pr):
        send_pr_comment(pr, check_prefixes(item))


if __name__ == '__main__':
    prs = get_all_user_prs('An11key', 'python_au', 'open')
    for item in prs:
        verify_pr(item)

