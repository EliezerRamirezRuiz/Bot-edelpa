SP_HELPTEXT mandar_alertas


CREATE PROCEDURE MANDAR_ALERTAS
	AS BEGIN
		SELECT A.AlertName, A.AlertDescription,
		A.AlertID, C.ID, C.NOMBRE_DEL_CANAL
		FROM ALERTS A 
		INNER JOIN CANALES C ON C.AREA = A.AREA
		WHERE A.AlertActivo = 1;
	END


CREATE PROCEDURE ULTIMAS_ALERTAS
	AS BEGIN 
		SELECT TOP 10
		AlertName,
		AlertDescription,
		AlertActivo,
		AlertDate
		FROM ALERTS
		WHERE AlertActivo = 1 
		ORDER BY AlertDate DESC
	END


CREATE PROCEDURE OBTENERSTOCK 
	@CODIGOETIQUETA varchar(32)
AS
BEGIN
	DECLARE
	@CENTRO varchar(4),
	@MATERIAL varchar(18),
	@LOTE varchar(10)
	
	--OBTENERSTOCK 'EP100000000006000621850000500010'

	SELECT @CENTRO = SUBSTRING(@CODIGOETIQUETA,1,4)
	SELECT @MATERIAL = SUBSTRING(@CODIGOETIQUETA,5,22)
	SELECT @LOTE = SUBSTRING(@CODIGOETIQUETA,23,32)

	--SELECT @CENTRO CENTRO, @MATERIAL MATERIAL, @LOTE LOTE 
	
	SELECT  MAKTX
	, CLABS, MANDT
	, MATNR, CHARG
	FROM MCHB 
	WHERE MATNR = @MATERIAL
	AND CHARG = @LOTE
END


CREATE PROCEDURE APAGAR_ALERTAS
	@ID INT
	
AS
BEGIN

	-- APAGAR_ALERTAS 1

UPDATE BDsap.dbo.ALERTS
SET ALERTACTIVO = 0
WHERE AlertID = @ID 

END