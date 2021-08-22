"""

import behold_service.handler.custom_image_handler as custom_image_handler

#TODO crikey we need some unit tests for the custom handler look at serve\ts\torch_handler\unit_tests\test_base_handler.py as a guide
# currently throwing error E   ModuleNotFoundError: No module named 'captum'
def test_get_top_three_results_and_output_to_logs():
    results = [{'item1': 0.2, 'item2': 0.15, 'item3': 0.1, 'item4': 0.05}]
    top_results = custom_image_handler.get_top_three_results(results)
    assert (top_results == [])


"""