from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Customer(Base):
    __tablename__ = "tblcustomer"
    customer_id = Column(Integer, primary_key=True)
    customer_code = Column(String(25), nullable=False)
    customer_name = Column(String(50), nullable=False)
    contact = Column(String(15), nullable=False)
    address = Column(String(100), nullable=False)


class Invoice(Base):
    __tablename__ = "tblinvoice"
    invoice_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("tblcustomer.customer_id"), nullable=False)
    payment_type = Column(Integer, nullable=False)
    total_amount = Column(Float, nullable=False)
    amount_tendered = Column(Float, nullable=False)
    bank_account_name = Column(String(50), nullable=False)
    bank_account_number = Column(String(25), nullable=False)
    date_recorded = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("tbluser.user_id"), nullable=False)
    customer = relationship("Customer")
    user = relationship("User")


class Product(Base):
    __tablename__ = "tblproduct"
    product_id = Column(Integer, primary_key=True)
    produce_code = Column(String(25), nullable=False)
    product_name = Column(String(50), nullable=False)
    unit_id = Column(Integer, ForeignKey("tblproductunit.unit_id"), nullable=False)
    category_id = Column(
        Integer, ForeignKey("tlbproductcategory.category_id"), nullable=False
    )
    unit_in_stock = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    reorder_level = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("tbluser.user_id"), nullable=False)
    unit = relationship("ProductUnit")
    category = relationship("ProductCategory")
    user = relationship("User")


class ProductUnit(Base):
    __tablename__ = "tblproductunit"
    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(String(15), nullable=False)


class PurchaseOrder(Base):
    __tablename__ = "tblpurchaseorder"
    purchase_order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("tblproduct.product_id"), nullable=False)
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    sub_total = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey("tblsupplier.supplier_id"), nullable=False)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("tbluser.user_id"), nullable=False)
    product = relationship("Product")
    supplier = relationship("Supplier")
    user = relationship("User")


class User(Base):
    __tablename__ = "tbluser"
    user_id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    fullname = Column(String(50), nullable=False)
    designation = Column(Integer, nullable=False)
    contact = Column(String(15), nullable=False)
    account_type = Column(Integer, nullable=False)


class ProductCategory(Base):
    __tablename__ = "tlbproductcategory"
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(25), nullable=False)


class Supplier(Base):
    __tablename__ = "tblsupplier"
    supplier_id = Column(Integer, primary_key=True)
    supplier_code = Column(String(15), nullable=False)
    supplier_name = Column(String(50), nullable=False)
    supplier_contact = Column(String(15), nullable=False)
    supplier_address = Column(String(100), nullable=False)
    supplier_email = Column(String(50), nullable=False)
