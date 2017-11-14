"""Fixing enum

Revision ID: 66f3910976d1
Revises: 2810e441086d
Create Date: 2017-11-08 10:47:46.727814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66f3910976d1'
down_revision = '2810e441086d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'contacts_location_id_fkey', 'contacts', type_='foreignkey')
    op.create_foreign_key(None, 'contacts', 'locations', ['location_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint(u'interfaces_firewall_id_fkey', 'interfaces', type_='foreignkey')
    op.drop_constraint(u'interfaces_network_id_fkey', 'interfaces', type_='foreignkey')
    op.drop_constraint(u'interfaces_host_id_fkey', 'interfaces', type_='foreignkey')
    op.create_foreign_key(None, 'interfaces', 'firewalls', ['firewall_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'interfaces', 'networks', ['network_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'interfaces', 'hosts', ['host_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint(u'locations_primary_contact_id_fkey', 'locations', type_='foreignkey')
    op.create_foreign_key(None, 'locations', 'contacts', ['primary_contact_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'locations', schema='public', type_='foreignkey')
    op.create_foreign_key(u'locations_primary_contact_id_fkey', 'locations', 'contacts', ['primary_contact_id'], ['id'])
    op.drop_constraint(None, 'interfaces', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'interfaces', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'interfaces', schema='public', type_='foreignkey')
    op.create_foreign_key(u'interfaces_host_id_fkey', 'interfaces', 'hosts', ['host_id'], ['id'])
    op.create_foreign_key(u'interfaces_network_id_fkey', 'interfaces', 'networks', ['network_id'], ['id'])
    op.create_foreign_key(u'interfaces_firewall_id_fkey', 'interfaces', 'firewalls', ['firewall_id'], ['id'])
    op.drop_constraint(None, 'contacts', schema='public', type_='foreignkey')
    op.create_foreign_key(u'contacts_location_id_fkey', 'contacts', 'locations', ['location_id'], ['id'])
    # ### end Alembic commands ###