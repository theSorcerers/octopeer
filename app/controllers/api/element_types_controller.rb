class Api::ElementTypesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def element_type_params
    params.require(:element_type).permit(:id, :name)
  end
end
