USE [BDPrincipal]
GO

/****** Object:  Table [dbo].[TB_Servidesk]    Script Date: 29/10/2023 20:14:07 ******/
--SET ANSI_NULLS ON
--GO

--SET QUOTED_IDENTIFIER ON
--GO

CREATE TABLE [dbo].[TBL_Servidesk](
	nTBLServideskID INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	cSolicitante nvarchar(255),
	cUsuario_Solicitante nvarchar(255),
	cCorreo_Solicitante nvarchar(255),
	cAsunto nvarchar(255) ,
	cEstado nvarchar(255) ,
	cCategoría nvarchar(255) ,
	cSubcategoria nvarchar(255) ,
	cTipo nvarchar(255) ,
	cModo nvarchar(255) ,
	cImpacto nvarchar(255) ,
	cUrgencia nvarchar(255) ,
	cPrioridad nvarchar(255) ,
	cAdjuntos bit,
	dHora_Creacion datetime,
	dHora_Resolucion datetime,
	dHora_Finalizacion datetime,
	cTecnico nvarchar(max),
	cResuelto_por nvarchar(max) ,
	cUsuario_PrimerNivel nvarchar(5) ,
	cUsuario_VIP bit,
	cReabiertos bit,
	cResolucion nvarchar(255) ,
	nTiempo float,
	cTiempoDias nvarchar(100) ,
	cSolicitanteRRHH nvarchar(max) ,
	cUsuario_SolicitanteRRHH nvarchar(5) ,
	cAgencia nvarchar(max) ,
	cCargo nvarchar(max) ,
	cCod_area nvarchar(5),
	cCod_age nvarchar(5),
	cArea nvarchar(max) ,
	cArticulo nvarchar(max) 
) 
GO


