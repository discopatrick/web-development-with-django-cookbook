import subprocess


def get_git_sha(repo_dir):
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                                   cwd=repo_dir).decode("utf-8").strip()
