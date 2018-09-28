-- config table for pkg configs
create table config (
  pkgid               integer primary key,
  pkgname             text,
  pkgversion          text,
  preconfigurescript  text,
  configurescript     text,
  postconfigurescript text,
  prebuildscript      text,
  buildscript         text,
  postbuildscript     text,
  preinstallscript    text,
  installscript       text,
  postinstallscript   text,
  downloadUrl         text,
  fileHash            text,
  dependency          integer,
  foreign key (dependency) references config (pkgid)
)