SYMBOLS: str = 'https://api.gemini.com/v1/symbols'
SYMBOL_DETAILS: str = 'https://api.gemini.com/v1/symbols/details/{symbol}'
NETWORK: str = 'https://api.gemini.com/v1/network/{token}'
PUBLIC_TICKER: str = 'https://api.gemini.com/v1/pubticker/{symbol}'
PUBLIC_TICKER_V2: str = 'https://api.gemini.com/v2/ticker/{symbol}'
CANDLES: str = 'https://api.gemini.com/v2/candles/{symbol}/{time_frame}'
FREE_PROMOS: str = 'https://api.gemini.com/v1/feepromos'
CURRENT_ORDER_BOOK: str = 'https://api.gemini.com/v1/book/{symbol}?limit_bids={bid_limit}&limit_asks={ask_limit}'
TRADE_HISTORY: str = 'https://api.gemini.com/v1/trades/{symbol}?limit_trades={limit_trades}&include_breaks={include_breaks}'
PRICE_FEED: str = 'https://api.gemini.com/v1/pricefeed'
