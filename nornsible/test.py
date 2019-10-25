import sys
from pathlib import Path
from unittest.mock import patch

from nornir import InitNornir
from nornir.core.task import AggregatedResult, MultiResult, Result

import nornsible
from nornsible import (
    InitNornsible,
    nornsible_task_message,
    parse_cli_args,
    patch_config,
    patch_inventory,
    print_result,
)

TEST_DIR='../tests/'

def test_patch_inventory_limit_host_ignore_case():
    args = ["-l", "UPPER-HOST"]
    args = parse_cli_args(args)
    nr = InitNornir(
        inventory={
            "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
            "options": {
                "host_file": f"{TEST_DIR}_test_nornir_inventory/hosts.yaml",
                "group_file": f"{TEST_DIR}_test_nornir_inventory/groups.yaml",
            },
        },
        logging={"enabled": False},
    )
    nr.inventory = patch_inventory(args, nr.inventory)
    assert set(nr.inventory.hosts.keys()) == {"upper-host"}

def main():
    test_patch_inventory_limit_host_ignore_case()

if __name__ == "__main__":
    main()