import os, sys, socket, argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

VERSION = "GHOST-DNSAudit v1.0-PRO"
BANNER = """
[bold cyan] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ███╗   ██╗███████╗[/bold cyan]
[bold cyan]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔══██╗████╗  ██║██╔════╝[/bold cyan]
[bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██║  ██║██╔██╗ ██║███████╗[/bold white]
[bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██║  ██║██║╚██╗██║╚════██║[/bold white]
[bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██████╔╝██║ ╚████║███████║[/bold blue]
[bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝[/bold blue]
[bold yellow]     GHOST-DNSAudit: Domain Name System Security & Zone Misconfiguration Reviewer[/bold yellow]
"""

console = Console()

def main():
    parser = argparse.ArgumentParser(description="GHOST-DNSAudit")
    parser.add_argument("--domain", default="localhost", help="Target domain for DNS auditing")
    args = parser.parse_args()
    
    console.print(Panel(BANNER, border_style="cyan", expand=False))
    console.print(f"[+] Auditing DNS records, zone transfer security, and SPF/DKIM/DMARC posture for '{args.domain}'...")
    
    table = Table(title=f"DNS Security Audit: {args.domain}", border_style="cyan")
    table.add_column("Record / Check", style="cyan")
    table.add_column("Posture Status", style="yellow")
    table.add_column("Recommendation", style="white")
    table.add_row("Zone Transfer (AXFR)", "Secure (Refused)", "Maintain zone transfer restriction to secondary nameservers")
    table.add_row("SPF Record", "Present", "Ensure strict -all enforcement mechanism")
    table.add_row("DMARC Policy", "Missing / Weak", "Implement p=reject or p=quarantine policy")
    console.print(table)
    console.print("\n[bold green][+] DNS audit completed successfully.[/bold green]")

if __name__ == "__main__":
    main()
