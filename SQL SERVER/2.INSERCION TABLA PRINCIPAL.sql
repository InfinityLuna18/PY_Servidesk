DECLARE @nCONT INT = (SELECT MIN(ID_CASO) FROM TB_Servidesk1$)
DECLARE @nCANT INT = (SELECT MAX(ID_CASO) FROM TB_Servidesk1$)
DECLARE @nID INT

WHILE (@nCONT<=@nCANT)
BEGIN
	SELECT @nID = ID_CASO
	FROM TB_Servidesk1$
	WHERE ID_CASO = @nCONT

	INSERT INTO TBL_Servidesk(
	cSolicitante
	,cUsuario_Solicitante
	,cCorreo_Solicitante
	,cAsunto
	,cEstado
	,cCategoría
	,cSubcategoria
	,cTipo
	,cModo
	,cImpacto
	,cUrgencia
	,cPrioridad
	,cAdjuntos
	,dHora_Creacion
	,dHora_Resolucion
	,dHora_Finalizacion
	,cTecnico
	,cResuelto_por
	,cUsuario_PrimerNivel
	,cUsuario_VIP
	,cReabiertos
	,cResolucion
	,nTiempo
	,cTiempoDias
	,cSolicitanteRRHH
	,cUsuario_SolicitanteRRHH
	,cAgencia
	,cCargo
	,cCod_area
	,cCod_age
	,cArea
	,cArticulo)
	SELECT
		Solicitante
		,Usuario_Solicitante
		,Correo_Solicitante
		,Asunto
		,Estado
		,Categoría
		,Subcategoria
		,Tipo
		,Modo
		,Impacto
		,Urgencia
		,Prioridad
		,Adjuntos
		,Hora_Creacion
		,Hora_Resolucion
		,Hora_Finalizacion
		,Tecnico
		,Resuelto_por
		,Usuario_PrimerNivel
		,Usuario_VIP
		,Reabiertos
		,Resolucion
		,Tiempo
		,TiempoDias
		,SolicitanteRRHH
		,Usuario_SolicitanteRRHH
		,Agencia
		,Cargo
		,Cod_area
		,Cod_age
		,Area
		,Articulo
	FROM TB_Servidesk1$
	WHERE ID_CASO = @nID

	SET @nCONT = @nCONT + 1

END



