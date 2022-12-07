vic()
{
    docker run --rm -it -v "$(pwd)":/host_path -w /host_path -e XDG_CONFIG_HOME='/root/.config/' qq905713813/luke-vim:latest vim $*
}
