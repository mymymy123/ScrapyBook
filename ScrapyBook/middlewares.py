# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import aiohttp
import asyncio
import logging

class AuthorizationMiddleware(object):

    accountpool_url='http://localhost:6789/antispider7/random'
    logger=logging.getLogger('middleware.authorization')
    async def process_request(self,request,spider):
        async with aiohttp.ClientSession() as client:
            response=await client.get(self.accountpool_url)
            if not response.status==200:
                return
            authorization=await response.text()
            self.logger.debug(f'set authorization jwt {authorization}')
            request.headers['authorization']=f'jwt {authorization}'
        



class ProxyMiddleware(object):
    proxypool_url='http://localhost:5555/random'
    logger=logging.getLogger('middlewares.proxy')
    async def process_request(self,request,spider):
        async with aiohttp.ClientSession() as client:
            response=await client.get(self.proxypool_url)
            if not response.status==200:
                return
            proxy=await response.text()
            self.logger.debug(f'set proxy {proxy}')
            request.meta['proxy']=f'http://{proxy}'