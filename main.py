from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()

# initialize server
mcp = FastMCP("ai2sql")

@mcp.tool()
async def generate_sql(request: str, table_name: str = None, columns: str = None):
    """
    Generates a basic SQL query based on the request.
    
    Args:
    request: Description of the SQL operation (e.g., "find all users", "create a table for products")
    table_name: Optional name of the table to query or create
    columns: Optional comma-separated list of column names with types for table creation
    
    Returns:
    A generated SQL query based on the request
    """
    request = request.lower()
    
    # Handle SELECT queries
    if any(word in request for word in ["select", "find", "get", "retrieve", "show"]):
        if not table_name:
            return "ERROR: Table name is required for SELECT queries"
        
        if "count" in request or "how many" in request:
            return f"SELECT COUNT(*) FROM {table_name};"
        
        if columns:
            selected_columns = columns
        else:
            selected_columns = "*"
            
        query = f"SELECT {selected_columns} FROM {table_name}"
        
        # Add WHERE clause if conditions mentioned
        if any(word in request for word in ["where", "filter", "condition"]):
            # Simple condition parsing
            if "equal" in request or "=" in request or "is" in request:
                parts = request.split("where", 1)[1] if "where" in request else request
                for column in (columns.split(",") if columns else ["id"]):
                    column = column.strip().split()[0]  # Get just the column name
                    if column.lower() in parts.lower():
                        query += f" WHERE {column} = 'value'"
                        break
            else:
                query += " WHERE condition"
        
        return query + ";"
    
    # Handle CREATE TABLE
    if any(word in request for word in ["create table", "new table", "make table"]):
        if not table_name:
            return "ERROR: Table name is required for CREATE TABLE queries"
            
        if not columns:
            return f"CREATE TABLE {table_name} (\n  id INTEGER PRIMARY KEY,\n  name TEXT,\n  created_at TIMESTAMP\n);"
        
        column_definitions = []
        for col in columns.split(","):
            col = col.strip()
            if " " in col:  # If type is provided
                column_definitions.append(f"  {col}")
            else:  # Default to TEXT type
                column_definitions.append(f"  {col} TEXT")
        
        return f"CREATE TABLE {table_name} (\n  id INTEGER PRIMARY KEY,\n" + ",\n".join(column_definitions) + "\n);"
    
    # Handle INSERT
    if any(word in request for word in ["insert", "add", "create record"]):
        if not table_name:
            return "ERROR: Table name is required for INSERT queries"
            
        if not columns:
            return f"INSERT INTO {table_name} (name, value) VALUES ('example_name', 'example_value');"
        
        cols = [c.strip().split()[0] for c in columns.split(",")]  # Extract just column names
        values = ["'example_value'" for _ in cols]
        
        return f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES ({', '.join(values)});"
    
    # Handle UPDATE
    if any(word in request for word in ["update", "change", "modify"]):
        if not table_name:
            return "ERROR: Table name is required for UPDATE queries"
            
        if not columns:
            return f"UPDATE {table_name} SET column_name = 'new_value' WHERE condition;"
        
        cols = [c.strip().split()[0] for c in columns.split(",")]  # Extract just column names
        set_clauses = [f"{col} = 'new_value'" for col in cols[:1]]  # Use first column as example
        
        return f"UPDATE {table_name} SET {', '.join(set_clauses)} WHERE id = 1;"
    
    # Handle DELETE
    if any(word in request for word in ["delete", "remove", "drop record"]):
        if not table_name:
            return "ERROR: Table name is required for DELETE queries"
            
        return f"DELETE FROM {table_name} WHERE condition;"
    
    # Handle DROP TABLE
    if "drop table" in request:
        if not table_name:
            return "ERROR: Table name is required for DROP TABLE queries"
            
        return f"DROP TABLE {table_name};"
    
    # Default response for unrecognized requests
    return "Could not generate SQL. Please specify the type of query (SELECT, CREATE TABLE, INSERT, etc.)"

if __name__ == "__main__":
    mcp.run(transport="stdio")
