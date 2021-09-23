<xsl:template match="/">
	XSLT Version: <xsl:value-of select="system-property('xsl:version')"/>
	XSLT Vendor: <xsl:value-of select="system-property('xsl:vendor')"/>
	XSLT Vendor URL: <xsl:value-of select="system-property('xsl:vendor-url')"/>
</xsl:template>