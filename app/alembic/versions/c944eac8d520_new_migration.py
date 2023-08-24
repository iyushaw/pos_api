"""New Migration

Revision ID: c944eac8d520
Revises: 
Create Date: 2023-08-23 21:54:17.862295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c944eac8d520'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblcustomer',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('customer_code', sa.String(length=25), nullable=False),
    sa.Column('customer_name', sa.String(length=50), nullable=False),
    sa.Column('contact', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('tblproductunit',
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('unit_name', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('unit_id')
    )
    op.create_table('tblsupplier',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('supplier_code', sa.String(length=15), nullable=False),
    sa.Column('supplier_name', sa.String(length=50), nullable=False),
    sa.Column('supplier_contact', sa.String(length=15), nullable=False),
    sa.Column('supplier_address', sa.String(length=100), nullable=False),
    sa.Column('supplier_email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('supplier_id')
    )
    op.create_table('tbluser',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('designation', sa.Integer(), nullable=False),
    sa.Column('contact', sa.String(length=15), nullable=False),
    sa.Column('account_type', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('tlbproductcategory',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('tblinvoice',
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('payment_type', sa.Integer(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.Column('amount_tendered', sa.Float(), nullable=False),
    sa.Column('bank_account_name', sa.String(length=50), nullable=False),
    sa.Column('bank_account_number', sa.String(length=25), nullable=False),
    sa.Column('date_recorded', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['tblcustomer.customer_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tbluser.user_id'], ),
    sa.PrimaryKeyConstraint('invoice_id')
    )
    op.create_table('tblproduct',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('produce_code', sa.String(length=25), nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('unit_in_stock', sa.Float(), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('discount_percentage', sa.Float(), nullable=False),
    sa.Column('reorder_level', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['tlbproductcategory.category_id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['tblproductunit.unit_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tbluser.user_id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('tblpurchaseorder',
    sa.Column('purchase_order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('sub_total', sa.Float(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['tblproduct.product_id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['tblsupplier.supplier_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tbluser.user_id'], ),
    sa.PrimaryKeyConstraint('purchase_order_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblpurchaseorder')
    op.drop_table('tblproduct')
    op.drop_table('tblinvoice')
    op.drop_table('tlbproductcategory')
    op.drop_table('tbluser')
    op.drop_table('tblsupplier')
    op.drop_table('tblproductunit')
    op.drop_table('tblcustomer')
    # ### end Alembic commands ###
