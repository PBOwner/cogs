
from .modmail import ModMail

__red_end_user_data_statement__ = "This cog does not store any End User Data."


async def setup(bot):
    await bot.add_cog(AltDentifier(bot))
