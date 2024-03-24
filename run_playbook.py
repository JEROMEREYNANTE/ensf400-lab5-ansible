import subprocess

def run_playbook(playbook_path):
    cmd = ['ansible-playbook', playbook_path, '-i', './hosts.yml']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.stderr

if __name__ == "__main__":
    playbook_path = 'hello.yml'
    stdout, stderr = run_playbook(playbook_path)
    print("Playbook Output:")
    print(stdout)
    print("Errors if any:")
    print(stderr)

s