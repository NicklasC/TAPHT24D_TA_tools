from behave import given, when, then


@when(u'User adds first item to cart')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When User adds first item to cart')


@then(u'Cart should contain one item')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then Cart should contain one item')


@when(u'User removes first item from cart')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When User removes first item from cart')


@then(u'Cart should be empty')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then Cart should be empty')


@given(u'that I order {item}')
def step_impl(context, item):
    pass
    # raise NotImplementedError(u'STEP: Given that I order A')


@then(u'{number_of_items} book titles should be listed')
def step_impl(context, number_of_items):
    pass
    # raise NotImplementedError(u'STEP: Then number of book titles should be listed')

@then(u'the total order sum should be {expected_sum}')
def step_impl(context,expected_sum):
    pass
    #raise NotImplementedError(u'STEP: Then the total order sum should be 45')
