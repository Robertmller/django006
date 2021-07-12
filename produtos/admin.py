from django.contrib import admin


class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'preco', 'estoque')


class AvaliacaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)