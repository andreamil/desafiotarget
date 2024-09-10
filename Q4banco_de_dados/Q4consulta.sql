SELECT 
    c.id_cliente, 
    c.nome AS razao_social, 
    t.numero AS telefone,
    tt.descricao AS tipo_telefone
FROM 
    Clientes c
JOIN 
    Estados e ON c.id_estado = e.id_estado
JOIN 
    Telefones t ON c.id_cliente = t.id_cliente
JOIN 
    TiposTelefone tt ON t.id_tipo = tt.id_tipo
WHERE 
    e.codigo_estado = 'SP';