
# Easter Company - Demo Server

Our demo server repository is built to provide a framework for developing and deploying
standalone web applications without needing to worry about providing individual hosting
solutions for each web application.

Some dependencies may be submodules within this repository however some may be embedded in
this repository - for example the `clients` repository should always be available and
deployed; however the `tools` repository is just a luxury. Both will be available if you
recursively pull this repository. Neither will be available if you don't. Otherwise you
can pull this repository directly and then individually pull each of the dependencies
selectively.

The demo server is hosted here:
[eastercompany.eu](https://eastercompany.eu.pythonanywhere.com), please check it
out and play around with it yourself.

Some dependenices will need to be `--recursive` pulled or specifically pulled in-order
to be shown on a local deployment.
