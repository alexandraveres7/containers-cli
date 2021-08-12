import subprocess
import click


@click.group()
def cli():
  pass


@cli.command(help="Get the logs of the container")
@click.argument('name')
def logs(name):
    subprocess.run([f"sudo kubectl logs -f deployment/{name} -c {name}"], shell=True)


@cli.command(help="Enter the container")
@click.argument('name')
def enter(name):
    subprocess.run([f"sudo kubectl exec -it deployment/{name} -c {name} -- /bin/sh"], shell=True)


@cli.command(help="Restart the container")
@click.argument('name')
def restart(name):
  container_id = get_container_id(name)
  subprocess.run([f"docker container restart {container_id}"], shell=True)


def get_container_id(name):
  container_id = subprocess.run([f"docker ps | grep {name} | grep -v istio | grep harbor | cut -d ' ' -f1"], shell=True,
                                stdout=subprocess.PIPE, encoding="utf-8").stdout.replace("\n", '')
  return container_id