# Nginx

Todo - move to wiki

## Nginx

install this onto the host

emerge www-servers/nginx


### Dotnet / C#

```
# Make sure this is installed for eselect
emerge app-eselect/eselect-repository

# add the dotnet overlay
eselect repository enable dotnet

# do a sync
emerge --sync

# I like to have a symlink under /usr/local/portage/
cd /usr/local/portage
ln -s /var/db/repos/dotnet dotnet
```

```
# install dotnet sdk
emerge dev-dotnet/dotnetcore-sdk-bin
# check version
dotnet --version
```

todo see if pull request goes through for arm64 ebuild
