from pynetbox.core.query import Request
from pynetbox.core.endpoint import response_loader
from .base import BaseSubCommand, ProcKWArgsAction
from ..core.utils import app_model_by_loc
from ..views.tools import nbprint

SEARCH_MODELS = ['circuits.providers',
                    'circuits.circuits',
                    'dcim.sites',
                    'dcim.racks',
                    'dcim.rack_groups',
                    'dcim.device_types',
                    'dcim.devices',
                    'dcim.virtual_chassis',
                    'dcim.cables',
                    'dcim.power_feeds',
                    'ipam.vrfs',
                    'ipam.aggregates',
                    'ipam.prefixes',
                    'ipam.ip_addresses',
                    'ipam.vlans',
                    'secrets.secrets',
                    'tenancy.tenants',
                    'virtualization.clusters',
                    'virtualization.virtual_machines']


class SearchSubCommand(BaseSubCommand):
    """Search Netbox objects with the given searchterm.

    The List of search models can be modified in:
    $HOME/$CONF_DIR/config.py"""

    name = 'search'
    parser_kwargs = dict(help='Search Netbox Objects')

    def setup(self):

        self.parser.add_argument('app_model',
                                 type=str,
                                 nargs='?',
                                 help='Model location to search (app.model)')

        self.parser.add_argument('searchterm',
                            help='Search term')

    def run(self):
        """Run a search of Netbox objects and show a table view of results.

        example usage:
        - search all search modelss for 'server1':
          $ nbcli search server1
        - search the dcim.interfaces model for 'eth 1':
          $ nbcli search dcim.interfaces 'eth 1'"""

        def search(ep):
            req = Request(filters=dict(q=self.args.searchterm),
                          base=ep.url,
                          token=ep.token,
                          session_key=ep.session_key,
                          http_session=ep.api.http_session)

            rep = req._make_call(add_params=dict(limit=15))

            result = list()

            if rep.get('results'):
                result = response_loader(rep['results'], ep.return_obj, ep)

            return result


        self.nbprint = nbprint

        if self.args.app_model:
            modellist = [self.args.app_model]
        else:
            modellist = SEARCH_MODELS

        result_count = 0

        print('')
        for app_model in modellist:
            model = app_model_by_loc(self.netbox, app_model)
            result = search(model)
            full_count = model.count(self.args.searchterm)
            if len(result) > 0:
                result_count += 1
                print('{}\n{}'.format(app_model,'=' * len(app_model)))
                self.nbprint(result)
                if len(result) < full_count:
                    print('*** See all {} results: '.format(full_count) +
                          "'$ nbcli pynb {} filter {}' ***". \
                          format(app_model, self.args.searchterm))
                print('')
        if result_count == 0:
            self.logger.warning('No results found')
            print('')
