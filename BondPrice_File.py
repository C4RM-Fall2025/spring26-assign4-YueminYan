def getBondPrice(y,face,couponRate,m,ppy):
  sum_present_values = 0
  
  # Calculate periodic coupon payment
  periodic_coupon = face * couponRate / ppy
  
  # Calculate periodic yield
  periodic_yield = y / ppy
  
  # Total number of periods
  total_periods = m * ppy

  for t in range(1, total_periods + 1):
    # Determine the cash flow for the current period
    cash_flow = periodic_coupon
    if t == total_periods:
      cash_flow += face # Add face value only to the last payment

    # Calculate present value factor for the current period
    present_value_factor = (1 + periodic_yield)**-t

    # Add the present value of the cash flow to the total
    sum_present_values += cash_flow * present_value_factor

  return sum_present_values
