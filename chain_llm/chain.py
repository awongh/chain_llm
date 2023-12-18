from typing import List


class Chain:
    def __init__(self, links: List[str]):
        self.links: List[str] = links

    def run(self):
        # for each link pass in the messages
        result = self.iterate_links(self.links)
        return result

    def iterate_links(self, links):
        for link in self.links:
            # todo: recursively call for objects in links list
            if isinstance(link, list):
                result = self.iterate_links(link)
            else:
                # load messages
                link.pre_run_callback()
                result = link.run()
                # save messages
                link.post_run_callback()
        return result
