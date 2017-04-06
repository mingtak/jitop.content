# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
from zope.component import getMultiAdapter


class ContactUs(BrowserView):

    def __call__(self):

        portal = api.portal.get()
        context=self.context
        request = self.request
        authenticator=getMultiAdapter((context, request), name=u"authenticator")
        if not authenticator.verify():
            raise Unauthorized
        email = request.form.get('email')
        name = request.form.get('name')
        text = request.form.get('text')
        # 測試信件
        api.portal.send_email(
            recipient="andy@mingtak.com.tw",
            sender="noreply@amagroup.com.tw",
            subject="台灣醫美通聯盟 網站使用者來信",
            body="姓名: %s \nemail: %s \n來信內容: %s" % (name, email, text),
        )


class CoverView(BrowserView):

    template = ViewPageTemplateFile("template/cover_view.pt")

    def __call__(self):

        portal = api.portal.get()
        folderName = ['about', 'service', 'showcase', 'partner', 'media', 'news']
        self.results = {}

        for folderItem in folderName:
            self.results[folderItem] = []
            brain = portal[folderItem].getChildNodes()
            for item in brain:
                if item.Type() == 'Page':
                    self.results[folderItem].append(item)

        return self.template()
